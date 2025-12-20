"""
Text-to-Speech Service for BookWise.
Uses browser's Web Speech API for client-side TTS.
"""

import streamlit as st
import streamlit.components.v1 as components
import json
from typing import Optional


class TTSService:
    """
    Text-to-Speech service using browser's Web Speech API.
    Provides client-side audio synthesis without external APIs.
    """
    
    # Available voices (common across browsers)
    VOICES = {
        'default': {'name': 'Default', 'lang': 'en-US'},
        'uk': {'name': 'British English', 'lang': 'en-GB'},
        'au': {'name': 'Australian English', 'lang': 'en-AU'},
        'in': {'name': 'Indian English', 'lang': 'en-IN'},
    }
    
    @staticmethod
    def render_audio_player(
        text: str,
        title: str = "Audio Summary",
        show_controls: bool = True,
        auto_play: bool = False,
        voice_lang: str = 'en-US',
        rate: float = 1.0,
        pitch: float = 1.0
    ) -> None:
        """
        Render an audio player component with TTS controls.
        
        Args:
            text: Text to be spoken
            title: Title for the audio player
            show_controls: Whether to show speed/voice controls
            auto_play: Auto-start playback
            voice_lang: Voice language code
            rate: Speech rate (0.5 to 2.0)
            pitch: Voice pitch (0 to 2)
        """
        # Sanitize text for JavaScript
        safe_text = json.dumps(text)
        
        # Unique key for this player
        player_id = f"tts_player_{abs(hash(text[:50]))}"
        
        # Calculate estimated duration (avg 150 words per minute)
        word_count = len(text.split())
        duration_mins = round(word_count / 150, 1)
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: 'Inter', -apple-system, sans-serif; }}
            </style>
        </head>
        <body>
        <div id="{player_id}" style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        ">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <div style="
                        width: 48px; height: 48px; 
                        background: rgba(255,255,255,0.2); 
                        border-radius: 50%; 
                        display: flex; 
                        align-items: center; 
                        justify-content: center;
                        font-size: 24px;
                    ">🎧</div>
                    <div>
                        <div style="font-size: 16px; font-weight: 700; color: white;">{title}</div>
                        <div style="font-size: 12px; color: rgba(255,255,255,0.8);">~{duration_mins} min • {word_count} words</div>
                    </div>
                </div>
                <div id="{player_id}_status" style="
                    background: rgba(255,255,255,0.2);
                    padding: 6px 12px;
                    border-radius: 20px;
                    font-size: 12px;
                    color: white;
                ">Ready</div>
            </div>
            
            <!-- Progress Bar -->
            <div style="background: rgba(255,255,255,0.2); border-radius: 8px; height: 6px; margin-bottom: 16px; overflow: hidden;">
                <div id="{player_id}_progress" style="background: white; height: 100%; width: 0%; transition: width 0.3s ease; border-radius: 8px;"></div>
            </div>
            
            <!-- Controls -->
            <div style="display: flex; align-items: center; justify-content: center; gap: 16px;">
                <button onclick="rewind()" style="
                    background: rgba(255,255,255,0.2);
                    border: none;
                    width: 40px; height: 40px;
                    border-radius: 50%;
                    cursor: pointer;
                    font-size: 16px;
                    color: white;
                    transition: all 0.2s;
                ">⏮️</button>
                
                <button id="{player_id}_playbtn" onclick="toggle()" style="
                    background: white;
                    border: none;
                    width: 56px; height: 56px;
                    border-radius: 50%;
                    cursor: pointer;
                    font-size: 24px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                    transition: all 0.2s;
                ">▶️</button>
                
                <button onclick="stop()" style="
                    background: rgba(255,255,255,0.2);
                    border: none;
                    width: 40px; height: 40px;
                    border-radius: 50%;
                    cursor: pointer;
                    font-size: 16px;
                    color: white;
                    transition: all 0.2s;
                ">⏹️</button>
            </div>
            
            <!-- Speed Control -->
            <div style="display: flex; align-items: center; justify-content: center; gap: 8px; margin-top: 16px;">
                <span style="font-size: 12px; color: rgba(255,255,255,0.8);">Speed:</span>
                <button onclick="setRate(0.75)" id="{player_id}_rate_075" style="background: rgba(255,255,255,0.1); border: none; padding: 4px 10px; border-radius: 12px; color: white; font-size: 11px; cursor: pointer;">0.75x</button>
                <button onclick="setRate(1.0)" id="{player_id}_rate_100" style="background: rgba(255,255,255,0.3); border: none; padding: 4px 10px; border-radius: 12px; color: white; font-size: 11px; cursor: pointer;">1x</button>
                <button onclick="setRate(1.25)" id="{player_id}_rate_125" style="background: rgba(255,255,255,0.1); border: none; padding: 4px 10px; border-radius: 12px; color: white; font-size: 11px; cursor: pointer;">1.25x</button>
                <button onclick="setRate(1.5)" id="{player_id}_rate_150" style="background: rgba(255,255,255,0.1); border: none; padding: 4px 10px; border-radius: 12px; color: white; font-size: 11px; cursor: pointer;">1.5x</button>
            </div>
        </div>
        
        <script>
            const text = {safe_text};
            let utterance = null;
            let isPlaying = false;
            let currentRate = {rate};
            
            // Split text into sentences for better progress tracking
            const sentences = text.match(/[^.!?]+[.!?]+/g) || [text];
            let currentSentence = 0;
            
            function updateStatus(status) {{
                document.getElementById('{player_id}_status').textContent = status;
            }}
            
            function updateProgress(percent) {{
                document.getElementById('{player_id}_progress').style.width = percent + '%';
            }}
            
            function updatePlayButton(playing) {{
                document.getElementById('{player_id}_playbtn').textContent = playing ? '⏸️' : '▶️';
            }}
            
            function toggle() {{
                if (!('speechSynthesis' in window)) {{
                    alert('Text-to-speech is not supported in your browser.');
                    return;
                }}
                
                if (isPlaying) {{
                    speechSynthesis.pause();
                    isPlaying = false;
                    updatePlayButton(false);
                    updateStatus('Paused');
                }} else {{
                    if (speechSynthesis.paused) {{
                        speechSynthesis.resume();
                        isPlaying = true;
                        updatePlayButton(true);
                        updateStatus('Playing');
                    }} else {{
                        // Start fresh
                        currentSentence = 0;
                        speakNextSentence();
                    }}
                }}
            }}
            
            function speakNextSentence() {{
                if (currentSentence >= sentences.length) {{
                    isPlaying = false;
                    updatePlayButton(false);
                    updateStatus('Completed');
                    updateProgress(100);
                    return;
                }}
                
                utterance = new SpeechSynthesisUtterance(sentences[currentSentence]);
                utterance.lang = '{voice_lang}';
                utterance.rate = currentRate;
                utterance.pitch = {pitch};
                
                utterance.onstart = function() {{
                    isPlaying = true;
                    updatePlayButton(true);
                    updateStatus('Playing');
                }};
                
                utterance.onend = function() {{
                    currentSentence++;
                    const progress = Math.round((currentSentence / sentences.length) * 100);
                    updateProgress(progress);
                    speakNextSentence();
                }};
                
                utterance.onerror = function(e) {{
                    console.error('TTS Error:', e);
                    updateStatus('Error');
                }};
                
                speechSynthesis.speak(utterance);
            }}
            
            function stop() {{
                speechSynthesis.cancel();
                isPlaying = false;
                currentSentence = 0;
                updatePlayButton(false);
                updateStatus('Stopped');
                updateProgress(0);
            }}
            
            function rewind() {{
                speechSynthesis.cancel();
                currentSentence = Math.max(0, currentSentence - 2);
                if (isPlaying) {{
                    speakNextSentence();
                }}
                updateProgress(Math.round((currentSentence / sentences.length) * 100));
            }}
            
            function setRate(rate) {{
                currentRate = rate;
                // Update button styles
                ['075', '100', '125', '150'].forEach(r => {{
                    const rateVal = parseFloat(r.substring(0, 1) + '.' + r.substring(1)) || parseFloat(r) / 100;
                    const btn = document.getElementById('{player_id}_rate_' + r);
                    if (btn) {{
                        btn.style.background = (rate === rateVal) ? 'rgba(255,255,255,0.3)' : 'rgba(255,255,255,0.1)';
                    }}
                }});
                
                // If playing, restart with new rate
                if (isPlaying) {{
                    speechSynthesis.cancel();
                    speakNextSentence();
                }}
            }}
            
            // Cleanup on page unload
            window.addEventListener('beforeunload', function() {{
                speechSynthesis.cancel();
            }});
        </script>
        </body>
        </html>
        """
        
        # Use components.html for proper JavaScript execution
        components.html(html_content, height=220)
    
    @staticmethod
    def render_mini_player(text: str, label: str = "Listen") -> None:
        """Render a minimal inline TTS button."""
        safe_text = json.dumps(text)
        player_id = f"mini_tts_{abs(hash(text[:30]))}"
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{ font-family: 'Inter', -apple-system, sans-serif; background: transparent; }}
            </style>
        </head>
        <body>
        <button id="{player_id}" onclick="togglePlay()" style="
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 600;
            transition: all 0.2s;
        ">
            🔊 {label}
        </button>
        
        <script>
            const text = {safe_text};
            let utterance = null;
            let isPlaying = false;
            
            function togglePlay() {{
                const btn = document.getElementById('{player_id}');
                
                if (!('speechSynthesis' in window)) {{
                    alert('Text-to-speech not supported in your browser.');
                    return;
                }}
                
                if (isPlaying) {{
                    speechSynthesis.cancel();
                    isPlaying = false;
                    btn.textContent = '🔊 {label}';
                }} else {{
                    utterance = new SpeechSynthesisUtterance(text);
                    utterance.lang = 'en-US';
                    utterance.onend = function() {{
                        isPlaying = false;
                        btn.textContent = '🔊 {label}';
                    }};
                    utterance.onerror = function() {{
                        isPlaying = false;
                        btn.textContent = '🔊 {label}';
                    }};
                    speechSynthesis.speak(utterance);
                    isPlaying = true;
                    btn.textContent = '⏹️ Stop';
                }}
            }}
            
            // Cleanup on unload
            window.addEventListener('beforeunload', function() {{
                speechSynthesis.cancel();
            }});
        </script>
        </body>
        </html>
        """
        
        components.html(html_content, height=45)


def render_audio_summary(book_data: dict, summary_text: str) -> None:
    """
    Convenience function to render audio player for a book summary.
    
    Args:
        book_data: Book metadata (title, author)
        summary_text: The summary text to speak
    """
    title = f"Listen to {book_data.get('title', 'Book Summary')}"
    TTSService.render_audio_player(
        text=summary_text,
        title=title,
        show_controls=True
    )

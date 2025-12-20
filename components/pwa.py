"""
PWA Support Component for BookWise.
Injects manifest, service worker registration, and PWA meta tags.
"""

import streamlit as st
import streamlit.components.v1 as components


def inject_pwa_support() -> None:
    """Inject PWA meta tags, manifest link, and service worker registration."""
    
    pwa_html = """
    <!-- PWA Meta Tags -->
    <meta name="application-name" content="BookWise">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="default">
    <meta name="apple-mobile-web-app-title" content="BookWise">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="msapplication-TileColor" content="#667eea">
    <meta name="msapplication-tap-highlight" content="no">
    <meta name="theme-color" content="#667eea">
    
    <!-- Manifest -->
    <link rel="manifest" href="/static/manifest.json">
    
    <!-- Apple Touch Icons -->
    <link rel="apple-touch-icon" href="/static/icons/icon-152x152.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/static/icons/icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/icons/icon-192x192.png">
    <link rel="apple-touch-icon" sizes="167x167" href="/static/icons/icon-192x192.png">
    
    <!-- Favicon -->
    <link rel="icon" type="image/png" sizes="32x32" href="/static/icons/icon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/icons/icon-16x16.png">
    
    <!-- Splash screens for iOS -->
    <meta name="apple-mobile-web-app-capable" content="yes">
    
    <style>
        /* PWA Install Banner */
        .pwa-install-banner {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 16px 20px;
            display: none;
            justify-content: space-between;
            align-items: center;
            z-index: 9999;
            box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.2);
        }
        
        .pwa-install-banner.show {
            display: flex;
        }
        
        .pwa-install-banner .message {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        
        .pwa-install-banner .message span {
            font-size: 24px;
        }
        
        .pwa-install-banner .text h4 {
            font-size: 14px;
            font-weight: 700;
            margin: 0 0 4px 0;
        }
        
        .pwa-install-banner .text p {
            font-size: 12px;
            opacity: 0.9;
            margin: 0;
        }
        
        .pwa-install-banner .actions {
            display: flex;
            gap: 12px;
        }
        
        .pwa-install-banner button {
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        .pwa-install-banner .install-btn {
            background: white;
            color: #667eea;
        }
        
        .pwa-install-banner .install-btn:hover {
            transform: scale(1.05);
        }
        
        .pwa-install-banner .dismiss-btn {
            background: rgba(255, 255, 255, 0.2);
            color: white;
        }
    </style>
    
    <!-- PWA Install Banner -->
    <div id="pwa-install-banner" class="pwa-install-banner">
        <div class="message">
            <span>📚</span>
            <div class="text">
                <h4>Install BookWise</h4>
                <p>Add to home screen for quick access</p>
            </div>
        </div>
        <div class="actions">
            <button class="dismiss-btn" onclick="dismissPWABanner()">Not now</button>
            <button class="install-btn" onclick="installPWA()">Install</button>
        </div>
    </div>
    
    <script>
        // Service Worker Registration
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', async () => {
                try {
                    const registration = await navigator.serviceWorker.register('/static/sw.js', {
                        scope: '/'
                    });
                    console.log('[PWA] Service Worker registered:', registration.scope);
                } catch (error) {
                    console.log('[PWA] Service Worker registration failed:', error);
                }
            });
        }
        
        // PWA Install Prompt
        let deferredPrompt;
        
        window.addEventListener('beforeinstallprompt', (e) => {
            console.log('[PWA] Install prompt available');
            e.preventDefault();
            deferredPrompt = e;
            
            // Check if user dismissed before
            if (!localStorage.getItem('pwa-dismissed')) {
                setTimeout(() => {
                    document.getElementById('pwa-install-banner').classList.add('show');
                }, 3000);
            }
        });
        
        async function installPWA() {
            if (!deferredPrompt) {
                console.log('[PWA] No install prompt available');
                return;
            }
            
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            console.log('[PWA] Install outcome:', outcome);
            
            deferredPrompt = null;
            document.getElementById('pwa-install-banner').classList.remove('show');
        }
        
        function dismissPWABanner() {
            document.getElementById('pwa-install-banner').classList.remove('show');
            localStorage.setItem('pwa-dismissed', 'true');
        }
        
        // Track app installed
        window.addEventListener('appinstalled', () => {
            console.log('[PWA] App installed');
            document.getElementById('pwa-install-banner').classList.remove('show');
            deferredPrompt = null;
        });
        
        // Detect if running as PWA
        if (window.matchMedia('(display-mode: standalone)').matches) {
            console.log('[PWA] Running as installed app');
        }
    </script>
    """
    
    st.markdown(pwa_html, unsafe_allow_html=True)


def render_pwa_install_button() -> None:
    """Render a manual PWA install button for the UI."""
    
    st.markdown("""
    <button id="pwa-manual-install" onclick="installPWA()" style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 14px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.2s;
    ">
        📲 Install App
    </button>
    """, unsafe_allow_html=True)


def render_offline_indicator() -> None:
    """Render an offline indicator that shows when the user loses connection."""
    
    st.markdown("""
    <div id="offline-indicator" style="
        position: fixed;
        top: 60px;
        left: 50%;
        transform: translateX(-50%);
        background: #ef4444;
        color: white;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: none;
        z-index: 9999;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
    ">
        📴 You're offline
    </div>
    
    <script>
        function updateOnlineStatus() {
            const indicator = document.getElementById('offline-indicator');
            if (!navigator.onLine) {
                indicator.style.display = 'block';
            } else {
                indicator.style.display = 'none';
            }
        }
        
        window.addEventListener('online', updateOnlineStatus);
        window.addEventListener('offline', updateOnlineStatus);
        updateOnlineStatus();
    </script>
    """, unsafe_allow_html=True)

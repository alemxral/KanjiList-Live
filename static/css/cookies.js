document.addEventListener("DOMContentLoaded", function() {
    // Check if the user has already accepted cookies
    if (!document.cookie.split('; ').find(row => row.startsWith('cookieConsent='))) {
        document.getElementById('cookieConsentBanner').style.display = 'block';
    }

    // When the user clicks "Got it!", set the cookie and hide the banner
    document.getElementById('acceptCookies').addEventListener('click', function() {
        document.cookie = "cookieConsent=true; max-age=" + 60*60*24*365 + "; path=/";
        document.getElementById('cookieConsentBanner').style.display = 'none';
        enableScripts();
    });

    // Function to enable scripts that require consent
    function enableScripts() {
        var scripts = document.querySelectorAll('script[type="text/plain"]');
        scripts.forEach(function(script) {
            var s = document.createElement('script');
            s.type = 'text/javascript';
            if (script.src) {
                s.src = script.src;
            } else {
                s.textContent = script.innerHTML;
            }
            document.head.appendChild(s);
            script.parentNode.removeChild(script);
        });
    }

    // If consent has been given, enable the scripts immediately
    if (document.cookie.split('; ').find(row => row.startsWith('cookieConsent='))) {
        enableScripts();
    }
});

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

class WebApp(App):
    def build(self):
        from jnius import autoclass
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        WebView = autoclass('android.webkit.WebView')
        WebViewClient = autoclass('android.webkit.WebViewClient')
        activity = PythonActivity.mActivity
        
        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.getSettings().setDomStorageEnabled(True)
        webview.setWebViewClient(WebViewClient())
        activity.setContentView(webview)
        webview.loadUrl("file:///android_asset/index.html")
        return Widget()

if __name__ == '__main__':
    WebApp().run()

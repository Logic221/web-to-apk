main.py
from kivy.app import App
from kivy.uix.browser import WebView # 部分环境可能需要特定webview组件
from kivy.core.window import Window
from screenpy.view import WebView # 这里我们通常使用这种方式
# 或者最简单的方式，使用 Kivy 的原生支持
from kivy.uix.widget import Widget
from webbrowser import open as open_url

class WebApp(App):
    def build(self):
        # 这里的逻辑是告诉 App：启动时加载同目录下的 index.html
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

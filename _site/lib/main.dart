import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';


void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: Scaffold(
      body: SafeArea(
        child: WebView(
          initialUrl: "https://github.com/Mnar1399/AIGP.git",
          javascriptMode: JavascriptMode.unrestricted,
        ),
      ),
    ),
  ));
}




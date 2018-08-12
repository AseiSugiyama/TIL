import 'package:flutter/material.dart';
import 'CounterBLoC.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Flutter Demo',
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatelessWidget {
  String title;

  MyHomePage({this.title});
  CounterBloc counterBloc = CounterBloc();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
           Text(
              'You have pushed the button this many times:',
            ),
            // データストリームから現在のカウントを取得
            StreamBuilder<int>(
              stream: counterBloc.countString,
              builder: (context, snapshot) =>
                  Text(
                    snapshot.data.toString(),
                    style: Theme.of(context).textTheme.display1,
                  ),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
         // ボタンが押された時Streamに通知
        onPressed: () => counterBloc.counterAddition.add(null),
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
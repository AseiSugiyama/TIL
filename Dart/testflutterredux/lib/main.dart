import 'package:flutter/material.dart';
import 'package:redux/redux.dart';
import 'package:flutter_redux/flutter_redux.dart';

enum Actions { Increment }

int counterReducer(int state, dynamic action) {
  if (action == Actions.Increment) {
    return state + 1;
  }
  return state;
}

void main() {
  final store = new Store<int>(counterReducer, initialState: 0);
  runApp(new MyApp(store: store));
}

class MyApp extends StatefulWidget {
  final Store<int> store;
  // This widget is the root of your application.
  MyApp({Key key, this.store}) : super(key: key);

  @override
  _MyAppState createState() => new _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    final title = "Flutter Redux Demo";
    return new MaterialApp(
      title: title,
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new StoreProvider(
        store: widget.store,
        child: new Scaffold(
          appBar: new AppBar(
            title: new Text(title),
          ),
          body: new Center(
            child: new Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                new Text('You have pushed the button this many times:'),
                new StoreConnector<int, String>(
                  converter: (store) => store.state.toString(),
                  builder: (context, count) => new Text(
                        count,
                        style: Theme.of(context).textTheme.display1,
                      ),
                )
              ],
            ),
          ),
          floatingActionButton: new StoreConnector<int, VoidCallback>(
            converter: (store) {
              return () => store.dispatch(Actions.Increment);
            },
            builder: (context, callback) => new FloatingActionButton(
                  onPressed: callback,
                  tooltip: 'increment',
                  child: new Icon(Icons.add),
                ),
          ),
        ),
      ),
    );
  }
}

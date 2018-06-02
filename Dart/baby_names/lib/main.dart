import 'package:flutter/material.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget{
  const MyApp();
  
  @override
  Widget build(BuildContext context) {
      // TODO: implement build
      return MaterialApp(
        title: 'Baby Names',
        home: const MyHomePage(title: 'Baby Name Botes'),
        color: Colors.white,
      );
    }
}

class MyHomePage extends StatelessWidget{
  const MyHomePage({Key key, this.title}) : super(key:key);
  
  final String title;

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(title: Text(title)),
      body: StreamBuilder(
        stream: Firestore.instance.collection('baby').snapshots(),
        builder: (context, snapshot) {
          if(!snapshot.hasData) return const Text('Loading...');
          return ListView.builder(
            itemCount: snapshot.data.documents.length,
            padding: const EdgeInsets.only(top: 10.0),
            itemExtent: 55.0,
            itemBuilder: (context, index) => 
              _buildListItem(context, snapshot.data.documents[index]),
          );
        },
      ),
    );
  }

  Widget _buildListItem(BuildContext context, DocumentSnapshot document) {
    return ListTile(
      key: new ValueKey(document.documentID),
      title: Container(
        decoration: BoxDecoration(
          border: Border.all(color: const Color(0x80000000)),
          borderRadius: BorderRadius.circular(5.0),
        ),
        padding: const EdgeInsets.all(10.0),
        child: Row(
          children: <Widget>[
            Expanded(
              child: Text(document['name']),
            ),
            Text(
              document['votes'].toString(),
            )
          ],
        ),
      ),
      onTap: () => Firestore.instance.runTransaction( (transaction) async {
        DocumentSnapshot freshSnap = await transaction.get(document.reference);
        await transaction.update(freshSnap.reference, {'votes': freshSnap['votes'] + 1});
      }),
    );
  }
}

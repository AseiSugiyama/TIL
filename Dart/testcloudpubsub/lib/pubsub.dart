import 'service-account.dart';
import 'package:googleapis_auth/auth_io.dart' as auth;
import 'package:gcloud/pubsub.dart';
import 'dart:async';
import 'package:rxdart/rxdart.dart';

class CloudPublisher {
  final List<String> _scopes = []..addAll(PubSub.SCOPES);
  final _credentials = auth.ServiceAccountCredentials.fromJson(credential);
  String prefix;

  final _counterAdditionController = StreamController();
  Sink get counterAddition => _counterAdditionController.sink;
  BehaviorSubject<int> _count = BehaviorSubject<int>(seedValue: 0);
  Stream<int> get countString => _count.stream;

  CloudPublisher() {
    _counterAdditionController.stream.listen((addition) {
      _count.add(_count.value + 1);
    });
  }

  Future publish(String message) async {
    var client = await auth.clientViaServiceAccount(_credentials, _scopes);
    const project = 'testcloudpubsub-212303';
    var pubsub = PubSub(client, project);
    var topic = await pubsub.lookupTopic('test-topic');
    await topic.publishString(message);
  }
}

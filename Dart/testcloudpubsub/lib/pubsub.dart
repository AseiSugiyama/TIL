import 'service-account.dart';
import 'package:googleapis_auth/auth_io.dart' as auth;
import 'package:gcloud/pubsub.dart';
import 'dart:async';
import 'package:rxdart/rxdart.dart';

class CloudPublisher {
  final List<String> _scopes = []..addAll(PubSub.SCOPES);
  final _credentials = auth.ServiceAccountCredentials.fromJson(credential);
  String prefix;

  final _counterAdditionController = StreamController<int>();
  Sink get counterAddition => _counterAdditionController.sink;
  BehaviorSubject<int> _count = BehaviorSubject<int>(seedValue: 0);
  Stream<int> get count => _count.stream;
  Topic _topic;

  CloudPublisher() {
    _counterAdditionController.stream.listen((value) {
      _count.add(_count.value + value);
    });
    auth.clientViaServiceAccount(_credentials, _scopes).then((client) async {
      const project = 'testcloudpubsub-212303';
      var pubsub = PubSub(client, project);
      _topic = await pubsub.lookupTopic('test-topic');
    });
  }

  Future publish(String message) async {
    await _topic.publishString(message);
  }
}

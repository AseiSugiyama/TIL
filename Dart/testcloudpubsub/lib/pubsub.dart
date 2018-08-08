import 'service-account.dart';
import 'dart:io';
import 'package:googleapis_auth/auth_io.dart' as auth;
import 'package:gcloud/pubsub.dart';
import 'dart:async';

final jsonString = File("service-account.json").readAsStringSync();

class CloudPublisher {
  final List<String> _scopes = []..addAll(PubSub.SCOPES);
  final _credentials = auth.ServiceAccountCredentials.fromJson(credential);

  Future publish(String message) async {
    var client = await auth.clientViaServiceAccount(_credentials, _scopes);
    const project = 'testcloudpubsub-212303';
    var pubsub = PubSub(client, project);
    // var topic = await pubsub.createTopic('test-topic');
    var topic = await pubsub.lookupTopic('test-topic');
    await topic.publishString(message);
  }
}

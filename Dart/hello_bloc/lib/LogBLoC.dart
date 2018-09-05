import 'dart:async';

/// Write counter value to log stream.
class LogBloc {
  StreamSubscription<int> _subscription;

  void subscribe({Stream<int> stream}){
      _subscription = stream.listen((count) {
      print(count);
    });
  }
}

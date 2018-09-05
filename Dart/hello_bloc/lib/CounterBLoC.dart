import 'dart:async';
import 'package:rxdart/rxdart.dart';

class CounterBloc{
  StreamController counterAdditionController = StreamController();
  Sink get counterAddition => counterAdditionController.sink;
  BehaviorSubject<int> _count = BehaviorSubject<int>(seedValue: 0);
  Stream<int> get count => _count.stream;

  CounterBloc(){
    counterAdditionController.stream.listen( (addition) {
      _count.add(_count.value + 1);
    });
  }
}  

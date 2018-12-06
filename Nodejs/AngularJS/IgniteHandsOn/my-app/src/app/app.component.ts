import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  // styleUrls: ['./app.component.css']
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = '備品リスト';

  onClickMenu() {
    console.log('Menu Clicked');
  }
}

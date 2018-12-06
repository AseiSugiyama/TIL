import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { IgxNavbarModule } from 'igniteui-angular';
import 'hammerjs';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    IgxNavbarModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

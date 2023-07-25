import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { PostsComponent } from './components/posts/posts.component';
import { MainComponent } from './components/main/main.component';
import { SingleComponent } from './components/single/single.component';

@NgModule({
  declarations: [
    AppComponent,
    PostsComponent,
    MainComponent,
    SingleComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

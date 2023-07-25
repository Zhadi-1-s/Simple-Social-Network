import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PostsComponent } from './components/posts/posts.component';
import { MainComponent } from './components/main/main.component';

const routes: Routes = [
  {path:'',redirectTo:'/main',pathMatch:'full'},
  {path:'main',component:MainComponent},
  {path:'posts',component:PostsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


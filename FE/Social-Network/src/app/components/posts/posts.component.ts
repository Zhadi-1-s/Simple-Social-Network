import { Component } from '@angular/core';

import { Posts } from 'src/app/shared/posts';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent {

    public posts: Posts[] = [
      {
        id:1,
        title:'Bmw 5 series (F10)',
        description:'One of the best bmw 5 series in the world, 4.4. Engine dws ',
        views:0,
        photoUrl:'assets/F10.jpg'
      },
      {
        id:2,
        title:'Audi Rs7 Perfomance',
        description:'Beautifull Audi ever maded',
        views:0,
        photoUrl:'assets/Rs7.jpg'
      }
    ]

}

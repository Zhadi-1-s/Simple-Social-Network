import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
@Injectable({
  providedIn: 'root'
})
export class PostService {

  private apiUrl='ApiUrl'

  constructor(private http: HttpClient) { }

  getPosts(){
      return this.http.get(this.apiUrl)
  }

}

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = "http://127.0.0.1:5000/generate";

  constructor(private http: HttpClient) {}

  generateDiagram(userStory: string): Promise<any> {
    return this.http.post(this.apiUrl, { user_story: userStory }).toPromise();
  }
}

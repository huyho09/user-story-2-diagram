import { Component } from '@angular/core';
import { UserStoryFormComponent } from './components/user-story-form/user-story-form.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [UserStoryFormComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
}

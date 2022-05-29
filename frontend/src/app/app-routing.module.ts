import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProfileComponent } from './profile/profile.component';
import { SavedPostsComponent } from './saved-posts/saved-posts.component';
import { FeedComponent } from './feed/feed.component';

const routes: Routes = [
  { path: 'profile', component: ProfileComponent},
  { path: 'feed', component: FeedComponent},
  { path: 'savedposts', component: SavedPostsComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

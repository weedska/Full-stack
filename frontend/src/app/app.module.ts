import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MatDialogModule } from "@angular/material/dialog";
import { RegFormComponent } from './reg-form/reg-form.component'
import { AuthComponent } from './auth/auth/auth.component';


import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { Placeholder } from '@angular/compiler/src/i18n/i18n_ast';
import { StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { environment } from '../environments/environment';
import { reducers } from './reducers/index';
import { AuthModule } from './auth/auth.module';
import { HttpClientModule} from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AuthService } from './auth/service/auth.service';
import { ProfileComponent } from './profile/profile.component';
import { FeedComponent } from './feed/feed.component';
import { SavedPostsComponent } from './saved-posts/saved-posts.component';



@NgModule({
  declarations: [
    AppComponent,
    RegFormComponent,
    ProfileComponent,
    FeedComponent,
    SavedPostsComponent,

  ],
  imports: [
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AuthModule,
    BrowserAnimationsModule,
    BrowserModule,
    AppRoutingModule,
    StoreModule.forRoot(reducers, {}),
    StoreDevtoolsModule.instrument({ maxAge: 25, logOnly: environment.production })
  ],
  providers: [],
  bootstrap: [AppComponent,]
})
export class AppModule { }

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthComponent } from './auth/auth.component';
import { MatDialogModule } from '@angular/material/dialog';
import { StoreModule } from '@ngrx/store';
import * as fromAuth from './reducers';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { authReducer } from './reducers/index';
import { AppRoutingModule } from './app-routing.module';



@NgModule({
  declarations: [
    AuthComponent,

  ],

  exports: [
    AuthComponent
  ],

  providers: [],

  imports: [

    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatDialogModule,
    CommonModule,
    AppRoutingModule,
    StoreModule.forFeature('auth', authReducer)
  ]
})
export class AuthModule { }

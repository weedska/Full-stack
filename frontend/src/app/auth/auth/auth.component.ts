import { Component, Injectable, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { RegFormComponent } from '../../reg-form/reg-form.component';
import { AuthService } from '../service/auth.service';
import { tap, map } from 'rxjs/operators';
import { Store } from '@ngrx/store';
import { AppState } from '../../reducers/index';
import { login, logout } from '../auth.actions';
import { User } from '../interface/user';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html',
  styleUrls: ['./auth.component.css'],
})
export class AuthComponent implements OnInit {

  form: FormGroup;

  $status: any = this.authService.userLoginStatus.subscribe(
    (res) => (this.$status = res));

  $userProfile: any = this.authService.userData.subscribe

  constructor(
    private router: Router,
    private dialog: MatDialog,
    private fb: FormBuilder,
    private authService: AuthService,
    private store: Store<AppState>
  ) {
    this.form = fb.group({
      username: ['pprzzi', [Validators.required]],
      password: ['Plskf415sdf', [Validators.required]],
    });
  }

  /// Checks on initiliazation if user is loged in
  isLogedIn() {
    /// if Token is in local storage, fetch user data ant sore it in Store
    if (localStorage.getItem('abc') != null) {
      this.authService
        .getUserData()
        .pipe(tap((user) => {this.store.dispatch(login({ user: user })),
                            this.authService.setUserProfile([user]),
                            this.authService.userData.subscribe((res) => this.$userProfile = res[0]
                            )
                            console.log(this.$userProfile)}))
        .subscribe(() => {
          this.authService.userLoginStatus.next(true);
        });
    } else {
      /// if Token in local storage is false then clear local storage
      localStorage.clear();
      this.authService.userLoginStatus.next(false);
    }
  }

  logOut() {
    localStorage.clear();
    this.store.dispatch(logout({ user: {} }));
    this.authService.userLoginStatus.next(false);
    this.authService.userData.next([]);
  }

  register() {
    const dialog = this.dialog.open(RegFormComponent);
    console.log('Logout form');


    dialog.afterClosed().subscribe((result) => {
      console.log(`Dialog result: ${result}`)

    });
  }






  ngOnInit(): void {
    this.isLogedIn();
  }
}

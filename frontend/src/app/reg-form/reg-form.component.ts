import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { tap } from 'rxjs/operators';
import { AuthService } from '../auth/service/auth.service';
import { Store } from '@ngrx/store';
import { AppState } from './../reducers/index';
import { login, logout } from '../auth/auth.actions';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { tokenReference } from '@angular/compiler';
import { Router } from '@angular/router';


@Component({
  selector: 'app-reg-form',
  templateUrl: './reg-form.component.html',
  styleUrls: ['./reg-form.component.css']
})
export class RegFormComponent implements OnInit {

  message = '';

  registerForm: FormGroup;
  loginForm: FormGroup;
  regLogin = 'log'

  constructor(private fb: FormBuilder,
              private router: Router,
              private authService: AuthService,
              private store: Store,
              private dialog: MatDialog,
              public regDialog: MatDialogRef<RegFormComponent>) {

    this.registerForm = fb.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]],
      repeatPassword: ['', [Validators.required]]
    })

    this.loginForm = fb.group({
      username: ['pprzzi', [Validators.required]],
      password: ['Plskf415sdf', [Validators.required]],
    })
  }


  register() {
    if (this.authService.checkPassMatch(this.registerForm.value['password'], this.registerForm.value['repeatPassword']) == true) {
      this.authService.register(this.registerForm.value['username'], this.registerForm.value['password'])
      .pipe(
        tap((token) => {
          localStorage.setItem('abc', token);

        })
      )
      .subscribe(
        () => {
          this.authService
            .getUserData()
            .pipe(tap((user) => {
                      this.authService.setUserProfile([user]),
                      this.store.dispatch(login({ user: user }))

                    }))
            .subscribe((res) => {

              this.authService.setUserStatus(true)
              this.regDialog.close('uzsidaro')




            });
        },
        (res) => this.message = res.error
      );
    }
    else {
      this.message = "Password doesn't match"
    }
  }


  login() {
    this.message = ''
    this.authService
      .login(this.loginForm.value['username'], this.loginForm.value['password'])
      .pipe(
        tap((token) => {
          localStorage.setItem('abc', token.token);
          window.location.reload();
        })
      )
      .subscribe(
        () => {
          this.authService
            .getUserData()
            .pipe(tap((user) =>{
              this.authService.setUserProfile([user]),
              this.store.dispatch(login({ user: user }))}
           ))
            .subscribe((res) => {
              this.authService.setUserStatus(true)
              this.regDialog.close('uzsidaro')
            });
        },
        (res) => this.message = res.error['non_field_errors']
      );
  }

  menuTab (status:string) {
    this.message = ''
    this.regLogin = status
  }

  ngOnInit(): void {
  }

}



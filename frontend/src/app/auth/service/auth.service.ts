import { Injectable } from '@angular/core';
import { User } from './../interface/user';
import { Observable, BehaviorSubject } from 'rxjs';
import { Token } from './../interface/user';
import { HttpClient} from '@angular/common/http';
import { tap, map } from 'rxjs/operators';
import { Store } from '@ngrx/store';
import { AppState } from '../../reducers/index';
import { logout } from '../auth.actions';


@Injectable({
  providedIn: 'root',
})
export class AuthService {

  userLoginStatus = new BehaviorSubject(false);
  userData = new BehaviorSubject(<User[]>{})

  private authUrl: string = 'https://www.pprzzi.com:8000/auth/';
  private userDetailUrl: string =
    'https://www.pprzzi.com:8000/users/users/user_detail/';
  private creatUserUrl: string = 'https://pprzzi.com:8000/users/add/create_user/';

  constructor(private http: HttpClient, private store: Store<AppState>) {}

  setUserStatus(status: boolean) {
    this.userLoginStatus.next(status);
  }

  setUserProfile(data: User[]) {
    this.userData.next(data)
  }

  login(user: string, password: string): Observable<Token> {
    return this.http.post<Token>(this.authUrl, {
      username: user,
      password: password,
    });
  }

  register(user: string, password: string): Observable<any> {
    return this.http.post(this.creatUserUrl, {
      username: user,
      password: password,
    });
  }

  checkPassMatch (pass1: string, pass2: string): boolean {
    if(pass1 === pass2) {
      return true
    }
    else {
      return false
    }
  }

  getUserData(): Observable<User> {
    console.log(localStorage.getItem('abc'))
    return this.http.get<User>(this.userDetailUrl, {
      headers: {
        'Content-type': 'application/json',
        Authorization: `Token ${localStorage.getItem('abc')}`,
      },
    });
  }

}

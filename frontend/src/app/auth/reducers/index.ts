import { User } from '../interface/user';
import {
  ActionReducer,
  ActionReducerMap,
  createFeatureSelector,
  createReducer,
  createSelector,
  MetaReducer,
  on
} from '@ngrx/store';
import { AuthActions } from '../action-types';
import { NONE_TYPE } from '@angular/compiler';



export const authFeatureKey = 'auth';

export interface AuthState {
  user: any
};

export const initialAuthState: AuthState =
{
  user: undefined
};

export const authReducer = createReducer(
  initialAuthState,

  on(AuthActions.login, (state, action) => {
    return {
      user: action.user
    };
  }),
  

  on(AuthActions.logout, (state, action) => {
    return {
      user: action.user
    }
  })
)





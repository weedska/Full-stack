import { createAction, props } from "@ngrx/store";
import { User } from './interface/user';


export const login = createAction(
  "[Header Index Page] User Login",
  props<{user: User}>()
);


export const logout = createAction(
  "[Header Index Page] User Logout",
  props<{user:{}}>()

)



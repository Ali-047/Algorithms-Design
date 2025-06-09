type signUpResponse = {
  id: number;
  last_login: string;
  is_superuser: boolean;
  first_name: string;
  last_name: string;
  is_staff: boolean;
  is_active: boolean;
  date_joined: string;
  email: string;
  name: string;
  username: string;
  groups: Array<string>;
  user_permissions: Array<string>;
};
type signUpRequest = {
  username: string,
  password: string,
  email: string,
  name: string
};
type loginRequest = {
  username: string;
  password: string;
}
type loginResponse = {
  refresh: string;
  access: string
}
export type { signUpResponse, signUpRequest,loginRequest, loginResponse};

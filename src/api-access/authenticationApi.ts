import HttpClient from "@/api-access/index.ts";
import type {
  loginRequest,
  loginResponse,
  signUpRequest,
  signUpResponse,
} from "@/types";
import type { AxiosResponse } from "axios";

export class AuthenticationApi {
  static postSignUpData(params: signUpRequest): Promise<signUpResponse> {
    return new Promise((resolve, reject) => {
      HttpClient.sendPostRequest("/api/register/", params)
        .then((response: AxiosResponse<signUpResponse>) => {
          console.log(response);
          resolve(response.data);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }

  static postLoginData(params: loginRequest): Promise<loginResponse> {
    return new Promise((resolve, reject) => {
      HttpClient.sendPostRequest("api/token/", params)
        .then((response: AxiosResponse<loginResponse>) => {
          resolve(response.data);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }

  static getUserInfo(id: object): Promise<object> {
    return new Promise((resolve, reject) => {
      HttpClient.sendGetRequest({ id }, "api/register/")
        .then((response: AxiosResponse<signUpResponse>) => {
          resolve(response.data);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }
}

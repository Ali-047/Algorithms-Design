import HttpClient from "@/api-access/index.ts";
import type { AxiosResponse } from "axios";

export class questionApi {
  static getQuestions(query: object): Promise<object> {
    return new Promise((resolve, reject) => {
      HttpClient.sendGetRequest(query, "api/start/questionnaire/")
        .then((response: AxiosResponse<object>) => {
          resolve(response.data);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }

  static sendUserAnswer(data: object): Promise<object> {
    return new Promise((resolve, reject) => {
      HttpClient.sendPostRequest("api/submit/answer/", data)
        .then((response: AxiosResponse<object>) => {
          resolve(response.data);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }
}

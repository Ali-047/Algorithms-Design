import HttpClient from "@/api-access/index.ts";
import type { AxiosResponse } from "axios";

export class fraudDetectionApi {
  static getFraudDetection(query: object): Promise<object> {
    return new Promise((resolve, reject) => {
      HttpClient.sendGetRequest(query, "api/similarity/")
        .then((response: AxiosResponse<object>) => {
          resolve(response.data);
        })
        .catch((error) => {
          reject(error);
        });
    });
  }
}

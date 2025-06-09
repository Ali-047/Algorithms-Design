import axios, { type AxiosResponse, type AxiosInstance } from "axios";
import { userData } from "@/stores/userData.ts";
import { toast } from "vue3-toastify";

type Interceptor = {
  onSuccess: (value: any) => any;
  onFailure: (value: any) => any;
};

export default class HttpClient {
  private static instance: HttpClient;
  axiosInstance: AxiosInstance;

  private constructor() {
    this.axiosInstance = axios.create({
      baseURL: "http://127.0.0.1:8000/",
      timeout: 5000,
    });
     const axiosInterceptorManager = new AxiosInterceptorManager();
    const requestInterceptor = axiosInterceptorManager.generateRequestInterceptor();
    const responseInterceptor = axiosInterceptorManager.generateResponseInterceptor();
    this.axiosInstance.interceptors.request.use(
      requestInterceptor.onSuccess,
      requestInterceptor.onFailure,
    );
    this.axiosInstance.interceptors.response.use(
      responseInterceptor.onSuccess,
      responseInterceptor.onFailure,
    );
  }

  static initialize(): void {
    HttpClient.instance = new HttpClient();
  }

  static getInstance(): HttpClient {
    if (!HttpClient.instance) {
      HttpClient.instance = new HttpClient();
    }
    return HttpClient.instance;
  }

  static sendGetRequest(
    query: object = {},
    url: string,
  ): Promise<AxiosResponse> {
    return HttpClient.instance.axiosInstance.request({
      method: "get",
      params: query,
      url: url,
    });
  }

  static sendPostRequest(url: string, data: object): Promise<AxiosResponse> {
    return HttpClient.instance.axiosInstance.request({
      method: "post",
      url: url,
      data: data,
    });
  }

  static sendPutRequest(
    query: object = {},
    url: string,
    data: object,
  ): Promise<AxiosResponse> {
    return HttpClient.instance.axiosInstance.request({
      method: "put",
      url: url,
      data: data,
      params: query,
    });
  }

  static sendDeleteRequest(
    query: object = {},
    url: string,
  ): Promise<AxiosResponse> {
    return HttpClient.instance.axiosInstance.request({
      method: "delete",
      params: query,
      url: url,
    });
  }
}

class AxiosInterceptorManager {
  generateRequestInterceptor(): Interceptor {
    return {
      onSuccess: (request: any): any => {
        const token = localStorage.getItem("token");
        if (token) {
          request.headers["Authorization"] = `JWT ${token}`;
        }
          return request;
      },
      onFailure: (error: any): any => {
        return Promise.reject(error);
      },
    };
  }

  generateResponseInterceptor(): Interceptor {
    return {
      onSuccess: (response: any): any => {
        return Promise.resolve(response);
      },
      onFailure: (error: any): any => {
        if (!error.response) {
          return Promise.reject(error);
        }

        const status = error.response.status;
        console.error(`⚠️ خطای ${status} دریافت شد`);
        if (status === 400){
          toast(error.response.data.error, {
            "theme": "dark",
            "type": "error",
            "position": "bottom-right",
            "pauseOnFocusLoss": false,
            "hideProgressBar": true,
            "transition": "slide"
          })
        }
        if (status === 401) {
          console.log("🚪 هدایت به صفحه ورود...");
          const store = userData();
          const router = useRouter();
          store.setUserName("");
          store.setEmail("");
          router.push("/login");
        } else if (status === 500) {
          console.log("💥 خطای سرور! صفحه رفرش می‌شود...");
          setTimeout(() => {
            window.location.reload();
          }, 5000);
        }

        return Promise.reject(error);
      },
    };
  }
}

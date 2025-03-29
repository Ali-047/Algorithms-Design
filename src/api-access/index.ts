import axios, {type AxiosResponse, type AxiosInstance} from "axios";

type Interceptor = {
    onSuccess: (value: any) => any,
    onFailure: (value: any) => any,
}

export default class HttpClient {
    private static instance: HttpClient;
    axiosInstance: AxiosInstance;

    private constructor() {
        this.axiosInstance = axios.create({
            baseURL: "/main",
            timeout: 5000,
        })
        const axiosInterceptorManager = new AxiosInterceptorManager()
        axios.interceptors.request.use(
            axiosInterceptorManager.generateRequestInterceptor().onSuccess,
            axiosInterceptorManager.generateRequestInterceptor().onFailure
        )
        axios.interceptors.response.use(
            axiosInterceptorManager.generateRequestInterceptor().onSuccess,
            axiosInterceptorManager.generateRequestInterceptor().onFailure
        )
    }

    static initialize(): void {
        HttpClient.instance = new HttpClient()
    }

    static getInstance(): HttpClient {
        if (!HttpClient.instance) {
            HttpClient.instance = new HttpClient()
        }
        return HttpClient.instance
    }

    static sendGetRequest(query: object = {}, url: string):
        Promise<AxiosResponse> {
        return HttpClient.instance.axiosInstance.request({
            method: 'get',
            params: query,
            url: url,
        })
    }

    static sendPostRequest(query: object = {}, url: string, data: object):
        Promise<AxiosResponse> {
        return HttpClient.instance.axiosInstance.request({
            method: 'post',
            url: url,
            data: data,
            params: query
        })
    }

    static sendPutRequest(query: object = {}, url: string, data: object):
        Promise<AxiosResponse> {
        return HttpClient.instance.axiosInstance.request({
            method: 'put',
            url: url,
            data: data,
            params: query
        })
    }

    static sendDeleteRequest(query: object = {}, url: string):
        Promise<AxiosResponse> {
        return HttpClient.instance.axiosInstance.request({
            method: 'delete',
            params: query,
            url: url
        })
    }
}

class AxiosInterceptorManager {
    generateRequestInterceptor():
        Interceptor {
        return {
            onSuccess: (request: any): any => {
                const token = localStorage.getItem("token");
                if (token) {
                    request.headers['Authorization'] = `JWT ${token}`
                    return request;
                }
            },
            onFailure: (error: any): any => {
                return Promise.reject(error);
            }
        }
    }

    generateDefaultResponseInterceptor():
        Interceptor {
        return {
            onSuccess: (response: any): any => {
                return Promise.resolve(response.data)
            },
            onFailure: (error: any): any => {
                if (!error.response) {
                    return Promise.reject(error);
                }

                const status = error.response.status;
                console.error(`⚠️ خطای ${status} دریافت شد`);

                if (status === 401) {
                    console.log("🚪 هدایت به صفحه ورود...");
                } else if (status === 500) {
                    console.log("💥 خطای سرور! صفحه رفرش می‌شود...");
                    setTimeout(() => {
                        window.location.reload();
                    }, 5000);
                }

                return Promise.reject(error);
            }
        }
    }
}

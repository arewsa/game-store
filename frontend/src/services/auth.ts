import { jwtDecode, type JwtPayload } from "jwt-decode";
import router from "../router/router";

async function refresh()
{
  const response = await fetch("http://localhost:8000/users/refresh", {
    method: "GET",
    credentials: "include",
  })
  const data = await response.json();
  if (await response.status == 401 || response.status == 422) {
    router.replace("/login");
    return null
  }
  sessionStorage.setItem("access_token", data.access_token);
  return true
}

export async function fetchWithCredentials(url: string, options: RequestInit) {
  let possible_token: string | null = sessionStorage.getItem("access_token")
  let access_token: JwtPayload | null = null;
  if (possible_token != null) {
    access_token = jwtDecode(possible_token);
  } 
  else {
    if (await refresh() == null) return null;
    possible_token = sessionStorage.getItem("access_token");
    if (possible_token != null) {
      access_token = jwtDecode(possible_token);
  }
}

  

  if (access_token != null && access_token.exp) {
    if (Date.now() >= access_token.exp * 1000) {
      await refresh();
      possible_token = sessionStorage.getItem("access_token");
    }
    if (!options.headers) {
      const headers: Headers = new Headers();
      options.headers = headers;
    }
    const headers: Headers = new Headers(options.headers);
    headers.set("Authorization", `Bearer ${possible_token}`);
    options.headers = headers;    
  }
  const response = await fetch(url, options);
  if (response.status == 401) {
    router.replace("/login");
    return null
  }
  return response;
}

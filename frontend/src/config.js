const url = import.meta.env.VITE_BACKEND_URL || "http://35.225.48.45:8080";
console.log("✅ BACKEND_URL:", url);
export const BACKEND_URL = url;

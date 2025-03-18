// 应用配置

// 获取环境变量中的API地址，如果未设置则使用自动检测的本机地址
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || (window.location.hostname === 'localhost' 
  ? `http://localhost:10012` 
  : `http://${window.location.hostname}:10012`);

// 应用标题
export const APP_TITLE = import.meta.env.VITE_APP_TITLE || 'AI Memoria';

// 是否显示网络连接状态组件（默认关闭）
export const SHOW_NETWORK_STATUS = import.meta.env.VITE_SHOW_NETWORK_STATUS === 'true';

// 当前API连接信息
export const getApiInfo = () => {
  return {
    baseUrl: API_BASE_URL,
    serverHost: API_BASE_URL.split('//')[1].split(':')[0],
    serverPort: API_BASE_URL.split(':').pop(),
    clientHost: window.location.hostname,
    clientPort: window.location.port
  };
};

export default {
  API_BASE_URL,
  APP_TITLE,
  SHOW_NETWORK_STATUS,
  getApiInfo
};
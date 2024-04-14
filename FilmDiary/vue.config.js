module.exports = {
    devServer: {
      proxy: {
        '/films': {
          target: 'http://127.0.0.1:8000',
          changeOrigin: true
        }
      }
    }
  };
  
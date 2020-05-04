export default {
  setIsAuthorized: (state, status) => {
    state.isAuthorized = status;
  },
  changeTheme: (state, newThemeName) => {
    state.theme = newThemeName;
  },
  changeLoaderStatus: (state, {status, message = ''}) => {
    state.loader = {
      status,
      message
    };
  },
};

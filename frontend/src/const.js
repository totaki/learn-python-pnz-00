const BASE_API_URL = `${process.env.REACT_APP_BASE_API || '/api/v1'}`;
const EVENTS = '/events';
const PLACES = '/places';
const AUTH_SUCCSESS = '/auth/success';

console.log(process.env.NODE_ENV, process.env.REACT_APP_BASE_API);
export {
  BASE_API_URL,
  EVENTS,
  PLACES,
  AUTH_SUCCSESS,
}
const BASE_API_URL = `${process.env.REACT_APP_BASE_API || '/api/v1'}`;
const EVENTS = '/public/events/';
const PLACES = '/public/places/';
const AUTH_SUCCESS = '/auth/success';
const PRIVATE_PLACES = '/private/places';

console.log(process.env.NODE_ENV, process.env.REACT_APP_BASE_API);
export {
  BASE_API_URL,
  EVENTS,
  PLACES,
  AUTH_SUCCESS,
  PRIVATE_PLACES,
}
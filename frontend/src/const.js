const BASE_API_URL = `${process.env.REACT_APP_BASE_API || '/api/v1'}`;
const EVENTS = '/public/events/';
const PLACES = '/public/places/';
const TAGS = '/public/tags/';
const AUTH_SUCCESS = '/auth/success';
const PRIVATE_PLACES = '/private/places';
const PRIVATE_EVENTS = '/private/events';

console.log(process.env.NODE_ENV, process.env.REACT_APP_BASE_API);
export {
  BASE_API_URL,
  EVENTS,
  PLACES,
  TAGS,
  AUTH_SUCCESS,
  PRIVATE_PLACES,
  PRIVATE_EVENTS,
}
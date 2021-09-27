import {BASE_API_URL, PRIVATE_PLACES} from "./const";

export const getItems = ({ url, path }, callback) => {
  const fullUrl = url || `${BASE_API_URL}${path}`;
  fetch(fullUrl)
    .then(result => result.json())
    .then(json => {
      callback(json);
    })
    .catch(e => console.log(e));
};

export const getPrivateItems = ({url, path, token }, callback) => {
  const fullUrl = url || `${BASE_API_URL}${path}`;
  fetch(fullUrl, {
    method: 'GET',
    headers: {
      'Content-type': 'application/json; charset=utf-8',
      'Authorization': `Token ${token}`
  },})
    .then(result => result.json())
    .then(json => {
      callback(json);
  })
    .catch(error => console.log(error));
  };

export const getTagItems = ({ url, path_tags }, callback) => {
  const fullUrl = url || `${BASE_API_URL}${path_tags}`;
  fetch(fullUrl)
    .then(result => result.json())
    .then(json => {
      callback(json);
    })
    .catch(e => console.log(e));
};

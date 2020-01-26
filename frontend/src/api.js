import {BASE_API_URL} from "./const";

export const getItems = ({ url, path }, callback) => {
  const fullUrl = url || `${BASE_API_URL}${path}`;
  fetch(fullUrl)
    .then(result => result.json())
    .then(json => {
      callback(json);
    })
    .catch(e => console.log(e));
};

import React, {useState, useEffect, useRef} from "react";
import {BASE_API_URL} from "./const";


const send = ({current}, callback) => {
  const getValue = name => {
    return current.elements.namedItem(name).value;
  };

  let place = {
    "place_name": getValue("place_name"),
    "city": getValue("city"),
    "street": getValue("street"),
    "house_number": getValue("house_number"),
    "office_number": getValue("office_number"),
  };
  const path = '/places/';
  const url = 'http://127.0.0.1:8000/api/v1/public/places/';
  const token = window.localStorage.getItem('token');
  // const full_token = 'Token '`${token}`;

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-type': 'application/json; charset=utf-8',
    },
    body: JSON.stringify(place)
  })
    .then(response => response.json())
    .then(json => callback(json));

};

// const Success_send = ({json}) => {
//   const name = json['result']['place_name'];
//   alert({name});
// };

function Send_place() {
  const [result, setResult] = useState({});
  const formRef = useRef(null);

  return (
    <form className="App" ref={formRef} id="_sone">
      <div className="form-row">
        <div className="form-group col-md-4">
          <label htmlFor="inputAddress">Место проведения</label>
          <input type="text" className="form-control" name="place_name" placeholder="Название"/>
        </div>
      </div>
      <div className="form-row">
        <div className="form-group col-md-4">
          <label htmlFor="inputCity">Город</label>
          <input type="text" className="form-control" name="city" />
        </div>
        <div className="form-group col-md-4">
          <label htmlFor="inputStreet">Улица</label>
          <input type="text" className="form-control" name="street" />
        </div>
        <div className="form-group col-md-2">
          <label htmlFor="inputHouse">Дом</label>
          <input type="text" className="form-control" name="house_number" />
        </div>
        <div className="form-group col-md-2">
          <label htmlFor="inputOffice">Офис</label>
          <input type="text" className="form-control" name="office_number" />
        </div>
      </div>
      <button type="submit" className="btn btn-primary" onClick={() => send(formRef, setResult)}>Send</button>
    </form>
  );
}

export default function Add_place() {

  return (
      <>
        <div className="container">
          <div className="my-h1">
            <h3 style={{textAlign: "center", marginBottom: 30, marginTop: 20}}>
              Форма для добавления Событий
            </h3>
          </div>
            <Send_place/>
        </div>
      </>
    )
}



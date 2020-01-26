import React, {useState, useEffect, useRef} from "react";
import {BASE_API_URL, PRIVATE_PLACES} from "./const";
import {getItems, getPrivateItems} from "./api";


function Send({ current }, callback){
// Функция send отправляет данные из формы в api

  const getValue = name => {
  //Функция для заполнения данными из формы объекта наподобие массива
    return current.elements.namedItem(name).value;
  };
}


function PushPlaces({place_name}) {
  return (<option>{place_name}</option>)
}

function SendEvent() {
// Здесь я объявляю переменные для отправки
  const [result, setResult] = useState({});
  const formRef = useRef(null);

//В этом блоке я подгружаю все известные места в форму
  const [places, setPlaces] = useState([]);
  const [path, _] = useState(PRIVATE_PLACES);
  const [url, setURL] = useState(null);
  const token = window.localStorage.getItem('token');

  useEffect(() => {
    getPrivateItems({ url, path, token }, (j) => setPlaces(j.results))
  }, [path]);
//
  return (
    <form>
      <div className="form-row">
        <div className="form-group col-md-6">
          <label htmlFor="input_event_name">Наименование события</label>
          <input
            className="form-control"
            name="title"
            type="text"
          />
        </div>
        <div className="form-group col-md-3">
          <p>
            <label htmlFor="input_date">Дата проведения</label>
            <input
              className="form-control"
              name="isEventDate"
              type="date_event"
            />
          </p>
        </div>
        <div className="form-group col-md-3">
          <p>
            <label htmlFor="input_time">Время начала</label>
            <input
              className="form-control"
              name="isEventTime"
              type="time_event"
            />
          </p>
        </div>
      </div>

      <div className="form-group">
        <div className="input-group">
          <div className="input-group-prepend">
            <span className="input-group-text">Описание события</span>
          </div>
          <textarea
            className="form-control"
            aria-label="input-group-text"
            name="body"
          />
        </div>
      </div>
      <div className="form-group">
        <label htmlFor="exampleFormControlSelect1">Example select</label>
        <select className="form-control" id="exampleFormControlSelect1" name="place">
          {places.map((e, i) => <PushPlaces {...e}/>)}
        </select>
      </div>
      <button type="submit" className="btn btn-primary" onClick={() => Send(formRef, setResult)}>Send</button>
    </form>
  );
}

function AddEvent() {
  return (
  <>
    <div className="container">
      <div className="my-h1">
        <h3 style={{textAlign: "center", marginBottom: 30, marginTop: 20}}>
          Форма для добавления Событий
        </h3>
      </div>
      <SendEvent />
    </div>
  </>
  )
}

export default AddEvent

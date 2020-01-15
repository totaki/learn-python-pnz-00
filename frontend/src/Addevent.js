import React, { useState, useEffect } from "react";
import { BASE_API_URL} from "./const";

const ADD_EVENT_ROUTE = 'add_event';

function Add_event() {
   return (
    <>
      <div className="container">
        <div className="my-h1"><h3 style={{textAlign: "center"}}>Форма для добавления Событий</h3></div>
        <form>
          <div className="form-row">
            <div className="form-group col-md-6">
              <label htmlFor="input_event_name">Наименование события</label>
              <input className="form-control" id="input_event_name"/>
            </div>
            <div className="form-group col-md-3">
              <p>
                <label htmlFor="input_date">Дата проведения</label>
                <input type="date" className="form-control" id="input_date"/>
              </p>
            </div>
            <div className="form-group col-md-3">
              <p>
                <label htmlFor="input_time">Время начала</label>
                <input type="time" className="form-control" id="input_time"/>
              </p>
            </div>
          </div>

          <div className="form-group">
            <div className="input-group">
              <div className="input-group-prepend">
                <span className="input-group-text">Описание события</span>
              </div>
              <textarea className="form-control" aria-label="input-group-text" id="input_body"></textarea>
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="inputAddress">Место проведения</label>
            <input type="text" className="form-control" id="input_place_name" placeholder="Название"/>
          </div>
          <div className="form-row">
            <div className="form-group col-md-4">
              <label htmlFor="inputCity">Город</label>
              <input type="text" className="form-control" id="input_сity"/>
            </div>
            <div className="form-group col-md-4">
              <label htmlFor="inputStreet">Улица</label>
              <input type="text" className="form-control" id="input_street"/>
            </div>
            <div className="form-group col-md-2">
              <label htmlFor="inputStreet">Дом</label>
              <input type="text" className="form-control" id="input_house_number"/>
            </div>
            <div className="form-group col-md-2">
              <label htmlFor="inputStreet">Офис</label>
              <input type="text" className="form-control" id="input_office_number"/>
            </div>
            <div className="form-group col-md-4">
              <label htmlFor="inputState">Тэги</label>
              <select id="inputTegs" className="form-control">
                <option selected>Choose...</option>
              </select>
            </div>
          </div>
          <button type="submit" className="btn btn-primary">Send</button>
        </form>
      </div>
    </>
  )
}

export default Add_event
export {
  ADD_EVENT_ROUTE
}
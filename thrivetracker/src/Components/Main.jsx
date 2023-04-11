import {Route, Routes} from 'react-router-dom'

import Home from './Home'
import Register from './Register'
import Login from './Login'
import Header from './Header'
import Nav from './Nav'
import Steps from './Steps'
import StepDetails from './StepDetails'
import Profile from './Profile'
import TimeTracker from './TimeTracker'
import MoneyTracker from './MoneyTracker'

export default function Main(){
    return(
        <div>
            <Routes>
                <Route path= "/" element= {<Home/>}/>
                <Route path = "/register" element = {<Register/>}/>
                <Route path = "/login" element = {<Login/>}/>
                <Route path = "/steps" element = {<Steps/>}/>
                <Route path = "/steps/:id" element = {<StepDetails/>}/>
                <Route path = "/profile" element = {<Profile/>}/>
                <Route path = "/timetracker" element = {<TimeTracker/>}/>
                <Route path = "/moneytracker" element = {<MoneyTracker/>}/>
                <Route path = "/nav" element = {<Nav/>}/>
                <Route path = "/header" element = {<Header/>}/>
            </Routes>
        </div>
    )
}
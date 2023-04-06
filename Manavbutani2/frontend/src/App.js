import { useState } from 'react';
import VMTLayout from './components/Layout';
import {BrowserRouter, Routes, Route} from "react-router-dom"
import CreateJiraTicket from './components/CreateJiraTicket';
import CreateVM from './components/CreateVM';
import UserDashboard from './components/UserDashboard';
import AdminDashboard from './components/AdminDashboard';
import PageNotFound from './components/PageNotFound';
import Login from './components/Login';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCircleUser, fas} from '@fortawesome/free-solid-svg-icons'
import { ADMIN_DASHBOARD, CREATE_ISSUE, CREATE_VM, LOGIN, USER_DASHBOARD } from './constants';
library.add(fas, faCircleUser)

function App() {

  const [selected, setSelected] = useState(["1"]);

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path={LOGIN} element={<Login />} />
          <Route path={USER_DASHBOARD} element={<VMTLayout selected={selected}><UserDashboard setSelected={setSelected}/></VMTLayout>}/>
          <Route path={ADMIN_DASHBOARD} element={<VMTLayout selected={selected}><AdminDashboard setSelected={setSelected}/></VMTLayout>}/>
          <Route path={CREATE_ISSUE} element={<VMTLayout selected={selected}><CreateJiraTicket setSelected={setSelected}/></VMTLayout>}/>
          <Route path={CREATE_VM} element={<VMTLayout selected={selected}><CreateVM /></VMTLayout>}/>
          <Route path='*' element={<PageNotFound />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

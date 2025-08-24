import React, { useState } from 'react'

function UserInfoForm({ onSubmit }) {
  const [form, setForm] = useState({
    name: '',
    location: '',
    email: '',
    phone: '',
    linkedin_link: '',
    linkedin_display: ''
  })

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if (onSubmit) onSubmit(form)
  }

  return (
    <div className="user-info-form">
      <h2>Enter Your Information</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" value={form.name} onChange={handleChange} />
        <input name="location" placeholder="Location" value={form.location} onChange={handleChange} />
        <input name="email" placeholder="Email" value={form.email} onChange={handleChange} />
        <input name="phone" placeholder="Phone" value={form.phone} onChange={handleChange} />
        <input name="linkedin_link" placeholder="LinkedIn Link" value={form.linkedin_link} onChange={handleChange} />
        <input name="linkedin_display" placeholder="LinkedIn Display" value={form.linkedin_display} onChange={handleChange} />
        <button type="submit" className="user-info-submit">Submit Info</button>
      </form>
    </div>
  )
}

export default UserInfoForm
# Be sure to restart your server when you modify this file.

# Your secret key for verifying cookie session data integrity.
# If you change this key, all old sessions will become invalid!
# Make sure the secret is at least 30 characters and all random, 
# no regular words or you'll be exposed to dictionary attacks.
ActionController::Base.session = {
  :key         => '_sochange_session',
  :secret      => '189052ba742c2aee1e2e3c027573aeef435a3b1d1c7d5ad7810711b44a6a711f1f261ec9f63c0a355c9a82b5e6a2f0082f7ee79d4de18ee953e1d5bbbd886e28'
}

# Use the database for sessions instead of the cookie-based default,
# which shouldn't be used to store highly confidential information
# (create the session table with "rake db:sessions:create")
# ActionController::Base.session_store = :active_record_store

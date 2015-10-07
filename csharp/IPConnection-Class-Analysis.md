# About

My goal for the refactoring of the `IPConnection` class is to have maintainable and understandable design for the C# (and .NET) language binding of Tinkerforge. One of the first steps is to understand how the current solution is organized and which features are implemented. Therefore this document provides an analysis of the existing solution.

This analysis talks a lot about the responsibilities of the involved classes. Here I follow the definition of responsibilities from [Uncle Bob](http://www.objectmentor.com/resources/articles/srp.pdf):

> In the context of the Single Responsibility Principle (SRP) we define a responsibility to be “a reason for change.” If you can think of more than one motive for changing a class, then that class has more than one responsibility.

To further elaborate on this: a class should have responsibility over a single part of the of the functionality provided by the software. So a responsibility describes a certain (part) of functionality, which has a reason to change.

# IPConnection class

The class `IPConnection` is more like a collection of classes. Although `IPConnection` is the main class providing the core API functionality, it contains several other classes. For an easier analysis, the next paragraphs analyse each class separately, although all classes are contained in `IPConnection`.

-	ToDo: What is the reason for having one class with several other classes contained in it?

## Methods

This section provides an overview of all methods of `IPConnection`:

-	`public void Connect(string host, int port)`
-	`private void ConnectUnlocked(bool isAutoReconnect)`
-	`public void Disconnect()`
-	`private void DisconnectUnlocked()`
-	`public void Authenticate(string secret)`
-	`public short GetConnectionState()`
-	`public void SetAutoReconnect(bool autoReconnect)`
-	`public bool GetAutoReconnect()`
-	`public void SetTimeout(int timeout)`
-	`public int GetTimeout()`
-	`public void Enumerate()`
-	`public void Wait()`
-	`public void Unwait()`
-	`internal int GetNextSequenceNumber()`
-	`private void ReceiveLoop(long localSocketID)`
-	`private void DispatchMeta(CallbackQueueObject cqo)`
-	`private void DispatchPacket(CallbackQueueObject cqo)`
-	`private void CallbackLoop(CallbackContext localCallback)`
-	`private void DisconnectProbeLoop(BlockingQueue<bool> localDisconnectProbeQueue)`
-	`internal static byte GetFunctionIDFromData(byte[] data)`
-	`internal static int GetLengthFromData(byte[] data)`
-	`internal static int GetUIDFromData(byte[] data)`
-	`internal static byte GetSequenceNumberFromData(byte[] data)`
-	`internal static bool GetResponseExpectedFromData(byte[] data)`
-	`internal static byte GetErrorCodeFromData(byte[] data)`
-	`private void HandleDisconnectByPeer(short disconnectReason, long socketID, bool disconnectImmediately)`
-	`private void HandleResponse(byte[] packet)`
-	`internal void SendRequest(byte[] request)`
-	`internal void AddDevice(Device device)`
